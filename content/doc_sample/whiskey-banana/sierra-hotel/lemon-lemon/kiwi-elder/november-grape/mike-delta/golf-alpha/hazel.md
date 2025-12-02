# Play: Hazel - setup

- hosts: all
  become: false
  vars:
    app_name: "hazel_app"
    retry_count: 1

  tasks:
    - name: Ensure date-task-1 is present
      ansible.builtin.file:
        path: /opt/hazel/date-task-1
        state: directory

    - name: Template date-task-1 config
      ansible.builtin.template:
        src: templates/date-task-1.j2
        dest: /etc/hazel/date-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart hazel service
      ansible.builtin.service:
        name: hazel
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
