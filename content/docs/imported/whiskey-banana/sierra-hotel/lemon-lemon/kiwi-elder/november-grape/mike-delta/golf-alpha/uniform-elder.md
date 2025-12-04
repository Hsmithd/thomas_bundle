# Play: Uniform - setup

- hosts: all
  become: true
  vars:
    app_name: "uniform_app"
    retry_count: 4

  tasks:
    - name: Ensure elder-task-1 is present
      ansible.builtin.file:
        path: /opt/uniform/elder-task-1
        state: directory

    - name: Template elder-task-1 config
      ansible.builtin.template:
        src: templates/elder-task-1.j2
        dest: /etc/uniform/elder-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart uniform service
      ansible.builtin.service:
        name: uniform
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z
