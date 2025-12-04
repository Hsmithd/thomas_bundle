# Play: Hazel - setup

- hosts: webservers
  become: false
  vars:
    app_name: "hazel_app"
    retry_count: 5

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/hazel/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/hazel/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure zulu-task-2 is present
      ansible.builtin.file:
        path: /opt/hazel/zulu-task-2
        state: directory

    - name: Template zulu-task-2 config
      ansible.builtin.template:
        src: templates/zulu-task-2.j2
        dest: /etc/hazel/zulu-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart hazel service
      ansible.builtin.service:
        name: hazel
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:43Z
