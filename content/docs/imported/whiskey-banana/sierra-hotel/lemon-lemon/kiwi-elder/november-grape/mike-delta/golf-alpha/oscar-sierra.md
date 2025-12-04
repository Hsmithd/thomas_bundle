# Play: Oscar - setup

- hosts: db
  become: false
  vars:
    app_name: "oscar_app"
    retry_count: 3

  tasks:
    - name: Ensure romeo-task-1 is present
      ansible.builtin.file:
        path: /opt/oscar/romeo-task-1
        state: directory

    - name: Template romeo-task-1 config
      ansible.builtin.template:
        src: templates/romeo-task-1.j2
        dest: /etc/oscar/romeo-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/oscar/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/oscar/golf-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure uniform-task-3 is present
      ansible.builtin.file:
        path: /opt/oscar/uniform-task-3
        state: directory

    - name: Template uniform-task-3 config
      ansible.builtin.template:
        src: templates/uniform-task-3.j2
        dest: /etc/oscar/uniform-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart oscar service
      ansible.builtin.service:
        name: oscar
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
